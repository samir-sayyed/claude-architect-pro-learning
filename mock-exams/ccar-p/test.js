'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const core=require('./exam.js');
const paths=['exam-data.json',...Array.from({length:5},(_,i)=>`sets/set-${String(i+2).padStart(2,'0')}/exam-data.json`)];
const forms=paths.map(path=>JSON.parse(fs.readFileSync(__dirname+'/'+path,'utf8')));
assert.equal(new Set(forms.map(d=>d.version)).size,6);
const storageKeys=new Set();
for (const data of forms) {
const perfect=Object.fromEntries(data.questions.map(q=>[q.id,q.options.flatMap((o,i)=>o.correct?[i]:[])]));
assert.equal(core.grade(data.questions,perfect).filter(g=>g.correct).length,63);
assert.equal(core.grade(data.questions,{}).filter(g=>g.correct).length,0);
const multi=data.questions.find(q=>q.select===2), single=data.questions.find(q=>q.select===1);
const right=perfect[multi.id], wrong=multi.options.findIndex(o=>!o.correct);
assert.equal(core.correct(multi,right.slice().reverse()),true);
assert.equal(core.correct(multi,[right[0]]),false);
assert.equal(core.correct(multi,[right[0],right[0]]),false);
assert.equal(core.correct(multi,[right[0],wrong]),false);
assert.equal(core.correct(multi,[...right,wrong]),false);
assert.deepEqual(core.choose(multi,right,wrong,true),right);
assert.deepEqual(core.choose(multi,right,right[0],false),[right[1]]);
assert.deepEqual(core.choose(single,[],0,true),[0]);
assert.deepEqual(core.choose(single,[0],1,true),[1]);
assert.deepEqual(core.choose(single,[0],99,true),[0]);
const attempt={version:data.version,started:1000,deadline:1000+data.minutes*60000,index:0,answers:perfect,flagged:[multi.id],submitted:null};
assert.equal(core.validate(attempt,data),true);
for(const patch of [{version:'old'},{index:-1},{index:63},{deadline:5},{answers:[]},{answers:{BAD:[0]}},{answers:{[multi.id]:[0,0]}},{answers:{[multi.id]:[99]}},{answers:{[multi.id]:[0,1,2]}},{flagged:['BAD']},{flagged:[multi.id,multi.id]},{submitted:2},{started:NaN}]) assert.equal(core.validate({...attempt,...patch},data),false,JSON.stringify(patch));
assert.equal(core.remaining(120000,0),120);
assert.equal(core.remaining(120000,119999),1);
assert.equal(core.remaining(120000,120000),0);
assert.equal(core.remaining(120000,130000),0);
assert.equal(core.complete(multi,[right[0]]),false);
assert.equal(core.complete(multi,right),true);
// Expired saved sessions must auto-submit during startup without a resume click.
const elements=new Map();
function el(id){if(!elements.has(id))elements.set(id,{id,hidden:false,textContent:'',innerHTML:'',value:'',open:false,children:[],classList:{toggle(){},remove(){}},addEventListener(){},focus(){},close(){this.open=false;},setAttribute(){}});return elements.get(id);}
el('exam-data').textContent=JSON.stringify(data);
const screens=['welcome','sitting','overview','results'].map(el);
let saved=JSON.stringify({...attempt,answers:{},deadline:attempt.deadline});
const context={document:{getElementById:el,querySelectorAll:s=>s==='[data-screen]'?screens:[]},localStorage:{getItem:key=>{storageKeys.add(key);return saved;},setItem:(_,v)=>saved=v},window:{scrollTo(){}},Date:class extends Date{static now(){return attempt.deadline+1000;}},setInterval(){},setTimeout(){},console};
vm.runInNewContext(fs.readFileSync(__dirname+'/exam.js','utf8'),context);
assert.equal(JSON.parse(saved).submitted,attempt.deadline+1000);
assert.equal(el('results').hidden,false);
assert.equal(el('sitting').hidden,true);
assert.equal(el('raw-score').textContent,'0 / 63');
assert.match(el('result-note').textContent,/Time expired/);
assert.equal(el('top-submit').hidden,true);
for(const other of forms.filter(d=>d.version!==data.version)) assert.equal(core.validate(attempt,other),false);
}
assert.equal(storageKeys.size,6);
console.log('PASS: all 6 forms: 378 perfect/empty scoring cases, exact sets, selection limits, invalid/cross-form states, isolated storage and expiry auto-submission.');

// Editorial shortcut diagnostics; these do not calibrate exam difficulty.
function combinations(n,k){let count=1;for(let i=1;i<=k;i++)count=count*(n-i+1)/i;return count;}
function extremeExpected(question,measure,longest){
    const sizes=question.options.map(o=>measure(o.text));
    const cutoff=[...sizes].sort((a,b)=>longest?b-a:a-b)[question.select-1];
    const forced=sizes.flatMap((size,i)=>(longest?size>cutoff:size<cutoff)?[i]:[]);
    const tied=sizes.flatMap((size,i)=>size===cutoff?[i]:[]);
    if(forced.some(i=>!question.options[i].correct) || question.options.some((o,i)=>o.correct&&!forced.includes(i)&&!tied.includes(i)))return 0;
    return 1/combinations(tied.length,question.select-forced.length);
}
const wordCount=text=>text.trim().split(/\s+/u).length;
const characterCount=text=>Array.from(text).length;
const tiedQuestion=(length,select)=>({select,options:Array.from({length},(_,i)=>({text:'tie',correct:i<select}))});
for(const measure of [wordCount,characterCount]){
    for(const longest of [true,false]){
        assert.equal(extremeExpected(tiedQuestion(4,1),measure,longest),.25);
        assert.equal(extremeExpected(tiedQuestion(5,2),measure,longest),.1);
    }
    assert.equal(extremeExpected({select:1,options:[{text:'short',correct:true},{text:'much longer',correct:false}]},measure,true),0);
    assert.equal(extremeExpected({select:1,options:[{text:'much longer',correct:true},{text:'short',correct:false}]},measure,false),0);
}
assert.equal(characterCount('a😀'),2);
const balanceForms=forms.slice(3);
const companionRoot=__dirname+'/../core-concept-learning/sets';
if(fs.existsSync(companionRoot))for(let n=1;n<=5;n++)balanceForms.push(JSON.parse(fs.readFileSync(companionRoot+`/set-${String(n).padStart(2,'0')}/exam-data.json`,'utf8')));
const revised=balanceForms.filter(data=>data.choice_balance_revision);
assert.equal(revised.length,balanceForms.length,'Every selected form needs the choice-balance revision tag');
const epsilon=1e-12;
for(const data of revised){
    const randomExpected=data.questions.reduce((total,q)=>total+1/combinations(q.options.length,q.select),0);
    assert.ok(Math.abs(randomExpected-12)<=epsilon,'Uniform random exact-set expectation must remain 12/63');
    for(const [label,measure] of [['words',wordCount],['characters',characterCount]]){
        const right=data.questions.flatMap(q=>q.options.filter(o=>o.correct).map(o=>measure(o.text)));
        const wrong=data.questions.flatMap(q=>q.options.filter(o=>!o.correct).map(o=>measure(o.text)));
        const ratio=(right.reduce((a,b)=>a+b,0)/right.length)/(wrong.reduce((a,b)=>a+b,0)/wrong.length);
        assert.ok(ratio>=.95-epsilon&&ratio<=1.05+epsilon,`${data.version}: correct/incorrect mean ${label} ratio ${ratio}`);
        for(const longest of [true,false]){
            const expected=data.questions.reduce((total,q)=>total+extremeExpected(q,measure,longest),0);
            assert.ok(expected<=16+epsilon,`${data.version}: ${longest?'longest':'shortest'}-only ${label} expectation ${expected}/63`);
        }
    }
}
if(revised.length)console.log(`PASS: ${revised.length} revised forms: word/codepoint mean ratios and tie-aware longest/shortest-only exact-set diagnostics.`);
