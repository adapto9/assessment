(function(t){function e(e){for(var r,n,i=e[0],s=e[1],u=e[2],c=0,d=[];c<i.length;c++)n=i[c],Object.prototype.hasOwnProperty.call(o,n)&&o[n]&&d.push(o[n][0]),o[n]=0;for(r in s)Object.prototype.hasOwnProperty.call(s,r)&&(t[r]=s[r]);p&&p(e);while(d.length)d.shift()();return l.push.apply(l,u||[]),a()}function a(){for(var t,e=0;e<l.length;e++){for(var a=l[e],r=!0,n=1;n<a.length;n++){var i=a[n];0!==o[i]&&(r=!1)}r&&(l.splice(e--,1),t=s(s.s=a[0]))}return t}var r={},n={app:0},o={app:0},l=[];function i(t){return s.p+"static/js/"+({upload:"upload"}[t]||t)+"."+{upload:"589fa98a"}[t]+".js"}function s(e){if(r[e])return r[e].exports;var a=r[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,s),a.l=!0,a.exports}s.e=function(t){var e=[],a={upload:1};n[t]?e.push(n[t]):0!==n[t]&&a[t]&&e.push(n[t]=new Promise((function(e,a){for(var r="static/css/"+({upload:"upload"}[t]||t)+"."+{upload:"b95d4230"}[t]+".css",o=s.p+r,l=document.getElementsByTagName("link"),i=0;i<l.length;i++){var u=l[i],c=u.getAttribute("data-href")||u.getAttribute("href");if("stylesheet"===u.rel&&(c===r||c===o))return e()}var d=document.getElementsByTagName("style");for(i=0;i<d.length;i++){u=d[i],c=u.getAttribute("data-href");if(c===r||c===o)return e()}var p=document.createElement("link");p.rel="stylesheet",p.type="text/css",p.onload=e,p.onerror=function(e){var r=e&&e.target&&e.target.src||o,l=new Error("Loading CSS chunk "+t+" failed.\n("+r+")");l.code="CSS_CHUNK_LOAD_FAILED",l.request=r,delete n[t],p.parentNode.removeChild(p),a(l)},p.href=o;var f=document.getElementsByTagName("head")[0];f.appendChild(p)})).then((function(){n[t]=0})));var r=o[t];if(0!==r)if(r)e.push(r[2]);else{var l=new Promise((function(e,a){r=o[t]=[e,a]}));e.push(r[2]=l);var u,c=document.createElement("script");c.charset="utf-8",c.timeout=120,s.nc&&c.setAttribute("nonce",s.nc),c.src=i(t);var d=new Error;u=function(e){c.onerror=c.onload=null,clearTimeout(p);var a=o[t];if(0!==a){if(a){var r=e&&("load"===e.type?"missing":e.type),n=e&&e.target&&e.target.src;d.message="Loading chunk "+t+" failed.\n("+r+": "+n+")",d.name="ChunkLoadError",d.type=r,d.request=n,a[1](d)}o[t]=void 0}};var p=setTimeout((function(){u({type:"timeout",target:c})}),12e4);c.onerror=c.onload=u,document.head.appendChild(c)}return Promise.all(e)},s.m=t,s.c=r,s.d=function(t,e,a){s.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,e){if(1&e&&(t=s(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(s.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)s.d(a,r,function(e){return t[e]}.bind(null,r));return a},s.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(e,"a",e),e},s.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},s.p="/",s.oe=function(t){throw console.error(t),t};var u=window["webpackJsonp"]=window["webpackJsonp"]||[],c=u.push.bind(u);u.push=e,u=u.slice();for(var d=0;d<u.length;d++)e(u[d]);var p=c;l.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"18db":function(t,e,a){"use strict";var r=a("53ed"),n=a.n(r);n.a},"53ed":function(t,e,a){},"56d7":function(t,e,a){"use strict";a.r(e);a("e260"),a("e6cf"),a("cca6"),a("a79d");var r=a("2b0e"),n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-app",[a("Navigation"),a("v-content",[a("v-container",{staticClass:"fill-height",attrs:{fluid:""}},[a("v-row",{attrs:{align:"center",justify:"center"}},[a("router-view")],1)],1)],1)],1)},o=[],l=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-container",[a("v-navigation-drawer",{attrs:{app:"",clipped:""},model:{value:t.drawer,callback:function(e){t.drawer=e},expression:"drawer"}},[a("v-list",{attrs:{dense:""}},[a("router-link",{attrs:{to:"/"}},[a("v-list-item",{attrs:{link:""}},[a("v-list-item-action",[a("v-icon",[t._v("mdi-view-dashboard")])],1),a("v-list-item-content",[a("v-list-item-title",[t._v("Dashboard")])],1)],1)],1),a("router-link",{attrs:{to:"/upload"}},[a("v-list-item",{attrs:{link:""}},[a("v-list-item-action",[a("v-icon",[t._v("mdi-publish")])],1),a("v-list-item-content",[a("v-list-item-title",[t._v("Upload")])],1)],1)],1)],1)],1),a("v-app-bar",{attrs:{app:"","clipped-left":""}},[a("v-app-bar-nav-icon",{on:{click:function(e){e.stopPropagation(),t.drawer=!t.drawer}}}),a("v-toolbar-title",[t._v("TechHunt 2020")])],1)],1)},i=[],s={data:function(){return{drawer:null}}},u=s,c=(a("18db"),a("2877")),d=a("6544"),p=a.n(d),f=a("40dc"),m=a("5bc1"),v=a("a523"),h=a("132d"),g=a("8860"),b=a("da13"),y=a("1800"),x=a("5d23"),w=a("f774"),C=a("2a7f"),S=Object(c["a"])(u,l,i,!1,null,"137b4cdc",null),V=S.exports;p()(S,{VAppBar:f["a"],VAppBarNavIcon:m["a"],VContainer:v["a"],VIcon:h["a"],VList:g["a"],VListItem:b["a"],VListItemAction:y["a"],VListItemContent:x["a"],VListItemTitle:x["b"],VNavigationDrawer:w["a"],VToolbarTitle:C["a"]});var _={components:{Navigation:V},created:function(){this.$vuetify.theme.dark=!0}},k=_,O=a("7496"),j=a("a75b"),L=a("0fd9"),E=Object(c["a"])(k,n,o,!1,null,null,null),T=E.exports;p()(E,{VApp:O["a"],VContainer:v["a"],VContent:j["a"],VRow:L["a"]});a("d3b7");var A=a("8c4f"),P=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("Dashboard")},N=[],D=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-container",[a("v-row",{staticClass:"text-center"},[a("v-col",{attrs:{cols:"12"}},[a("h1",{staticClass:"display-2 font-weight-bold mb-3"},[t._v("Dashboard")]),a("blockquote",{staticClass:"blockquote"},[t._v(t._s(t.response))])]),a("v-col",{attrs:{cols:"12"}},[a("v-card",{attrs:{flat:""}},[a("v-container",{attrs:{"grid-list-xl":"","text-xs-center":""}},[a("v-layout",{attrs:{row:"",wrap:""}},[a("v-flex",{attrs:{xs6:""}},[a("v-text-field",{attrs:{label:"Minimum Salary"},model:{value:t.minSalary,callback:function(e){t.minSalary=e},expression:"minSalary"}})],1),a("v-flex",{attrs:{xs6:""}},[a("v-text-field",{attrs:{label:"Maximum Salary"},model:{value:t.maxSalary,callback:function(e){t.maxSalary=e},expression:"maxSalary"}})],1),a("v-flex",{attrs:{xs6:""}},[a("v-select",{attrs:{items:t.columns,label:"Sort By"},model:{value:t.sortColumn,callback:function(e){t.sortColumn=e},expression:"sortColumn"}})],1),a("v-flex",{attrs:{xs6:""}},[a("v-select",{attrs:{items:t.orders,label:"Order"},model:{value:t.sortOrder,callback:function(e){t.sortOrder=e},expression:"sortOrder"}})],1)],1)],1)],1),a("v-btn",{attrs:{block:"",color:"primary",loading:t.loading},on:{click:function(e){return t.populate(!1)}}},[t._v("Search")])],1),a("v-col",{attrs:{cols:"12"}},[a("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.employees,loading:t.loading,page:t.page,"items-per-page":t.limit,"hide-default-footer":""},on:{"update:page":function(e){t.page=e}}}),a("div",{staticClass:"text-center pt-2"},[a("v-pagination",{attrs:{length:t.pageCount},model:{value:t.page,callback:function(e){t.page=e},expression:"page"}})],1)],1)],1)],1)},I=[],M=a("bc3a"),B=a.n(M),$={name:"Dashboard",data:function(){return{headers:[{text:"Id",align:"start",sortable:!1,value:"id"},{text:"Login",sortable:!1,value:"login"},{text:"Name",sortable:!1,value:"name"},{text:"Salary",sortable:!1,value:"salary"}],page:1,pageCount:0,minSalary:0,maxSalary:5e3,offset:0,limit:30,sortColumn:"Id",sortOrder:"Ascending",employees:[],response:null,loading:!1,columns:["Id","Login","Name","Salary"],orders:["Ascending","Descending"]}},computed:{sort:function(){return"Ascending"==this.sortOrder?"+"+this.sortColumn.toLowerCase():"-"+this.sortColumn.toLowerCase()}},watch:{page:function(){this.offset=(this.page-1)*this.limit,this.populate(!0)}},methods:{populate:function(t){var e=this;this.loading=!0,B.a.get("http://127.0.0.1:5000/users",{params:{minSalary:this.minSalary,maxSalary:this.maxSalary,offset:this.offset,limit:this.limit,sort:this.sort}}).then((function(a){e.loading=!1,0==t&&(a.data.count[0][0]%e.limit!=0?(console.log(a.data.count[0][0]),e.pageCount=Math.floor(a.data.count[0][0]/e.limit)+1):e.pageCount=Math.floor(a.data.count[0][0]/e.limit)),e.employees=a.data.results})).catch((function(t){e.loading=!1,e.response="Error code "+t.response.status+": "+t.response.data.results}))}},mounted:function(){this.populate(!1)}},q=$,H=a("8336"),F=a("b0af"),U=a("62ad"),J=a("8fea"),R=a("0e8f"),K=a("a722"),z=a("891e"),G=a("b974"),Q=a("8654"),W=Object(c["a"])(q,D,I,!1,null,null,null),X=W.exports;p()(W,{VBtn:H["a"],VCard:F["a"],VCol:U["a"],VContainer:v["a"],VDataTable:J["a"],VFlex:R["a"],VLayout:K["a"],VPagination:z["a"],VRow:L["a"],VSelect:G["a"],VTextField:Q["a"]});var Y={name:"Home",components:{Dashboard:X}},Z=Y,tt=Object(c["a"])(Z,P,N,!1,null,null,null),et=tt.exports;r["a"].use(A["a"]);var at=[{path:"/",name:"Home",component:et},{path:"/upload",name:"Upload",component:function(){return a.e("upload").then(a.bind(null,"2679"))}}],rt=new A["a"]({mode:"history",base:"/",routes:at}),nt=rt,ot=a("f309");r["a"].use(ot["a"]);var lt=new ot["a"]({});r["a"].config.productionTip=!1,new r["a"]({router:nt,vuetify:lt,render:function(t){return t(T)}}).$mount("#app")}});
//# sourceMappingURL=app.78386ec3.js.map