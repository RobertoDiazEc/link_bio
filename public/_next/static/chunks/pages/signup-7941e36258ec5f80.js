(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[252],{2546:(e,i,n)=>{(window.__NEXT_P=window.__NEXT_P||[]).push(["/signup",function(){return n(4180)}])},4180:(e,i,n)=>{"use strict";n.r(i),n.d(i,{Div_0c4c0d922d990c245023c72baae2d5e1:()=>S,Errorboundary_5bd40ca0d5b8bd76c9d87570fc6ec5c0:()=>N,Fragment_c179379f847dbcf00ba21f73b0ad1b3d:()=>H,Root_9ffb1e9a6f21b61bee7e82c67e82844a:()=>y,Toaster_6e6ebf8d7ce589d59b7d382fb7576edf:()=>k,default:()=>z});var t=n(4577),r=n(2445),o=n(6540),s=n(8526),c=n(7665),a=n(9188),l=n(2930),d=n(7437),h=n(5107),m=n(8929),x=n(1544),p=n(6491),g=n(3258),f=n(5236),u=n(4721),Y=n(749),w=n(8779),b=n(4767),v=n(1106),D=n.n(v),F=n(3368),C=n.n(F);function _(){let e=(0,t._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _=function(){return e},e}function H(){let[e,i]=(0,o.useContext)(a.EventLoopContext);return(0,r.Y)(o.Fragment,{children:(0,l.isTrue)(i.length>0)?(0,r.Y)(o.Fragment,{children:(0,r.Y)(h.A,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:V+" 1s infinite"},size:32})}):(0,r.Y)(o.Fragment,{})})}function k(){let{resolvedColorMode:e}=(0,o.useContext)(a.ColorModeContext);l.refs.__toast=u.oR;let[i,n]=(0,o.useContext)(a.EventLoopContext),t={description:"Check if server is reachable at "+(0,l.getBackendURL)(Y.ll).href,closeButton:!0,duration:12e4,id:"websocket-error"},[s,c]=(0,o.useState)(!1);return(0,o.useEffect)(()=>{n.length>=2?s||u.oR.error("Cannot connect to server: ".concat(n.length>0?n[n.length-1].message:"","."),{...t,onDismiss:()=>c(!0)}):(u.oR.dismiss("websocket-error"),c(!1))},[n]),(0,r.Y)(u.l$,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function y(){let[e,i]=(0,o.useContext)(a.EventLoopContext),n=(0,o.useCallback)(i=>{let n=i.target;i.preventDefault();let t={...Object.fromEntries(new FormData(n).entries())};!function(){for(var i=arguments.length,n=Array(i),r=0;r<i;r++)n[r]=arguments[r];e([(0,l.Event)("_call_function",{function:()=>window.alert(JSON.stringify(t)),callback:null},{})],n,{})}()});return(0,r.Y)(b.bL,{className:"Root ",css:{width:"100%"},onSubmit:n,children:(0,r.FD)(w.Tabs.Root,{css:{"&[data-orientation='vertical']":{display:"flex"},padding:"15px"},defaultValue:"tab1",children:[(0,r.FD)(w.Tabs.List,{css:{"&[data-orientation='vertical']":{display:"block",boxShadow:"inset -1px 0 0 0 var(--gray-a5)"}},children:[(0,r.Y)(w.Tabs.Trigger,{css:{"&[data-orientation='vertical']":{width:"100%"}},value:"tab1",children:"Datos Personales"}),(0,r.Y)(w.Tabs.Trigger,{css:{"&[data-orientation='vertical']":{width:"100%"}},value:"tab2",children:"Datos Ingreso"})]}),(0,r.Y)(w.Tabs.Content,{css:{"&[data-orientation='vertical']":{width:"100%",margin:null},padding:"15px"},value:"tab1",children:(0,r.FD)(w.Flex,{css:{width:"100%"},direction:"column",gap:"2",children:[(0,r.FD)(w.Flex,{css:{"@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"row"},"@media screen and (min-width: 48em)":{flexDirection:"row"}},gap:"3",children:[(0,r.Y)(b.D0,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"nombres",children:(0,r.FD)(w.Flex,{direction:"column",children:[(0,r.Y)(b.JU,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Nombres"}),(0,r.Y)(b.Ec,{asChild:!0,className:"Control ",children:(0,r.Y)(w.TextField.Root,{placeholder:"Nombres",type:"text"})})]})}),(0,r.Y)(b.D0,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"apellidos",children:(0,r.FD)(w.Flex,{direction:"column",children:[(0,r.Y)(b.JU,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Apellidos"}),(0,r.Y)(b.Ec,{asChild:!0,className:"Control ",children:(0,r.Y)(w.TextField.Root,{placeholder:"Apellidos",type:"text"})})]})})]}),(0,r.FD)(w.Flex,{css:{"@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"row"},"@media screen and (min-width: 48em)":{flexDirection:"row"}},gap:"3",children:[(0,r.Y)(b.D0,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"email",children:(0,r.FD)(w.Flex,{direction:"column",children:[(0,r.Y)(b.JU,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Email"}),(0,r.Y)(b.Ec,{asChild:!0,className:"Control ",children:(0,r.Y)(w.TextField.Root,{placeholder:"user@cpkm.com.co",type:"email"})})]})}),(0,r.Y)(b.D0,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"celular",children:(0,r.FD)(w.Flex,{direction:"column",children:[(0,r.Y)(b.JU,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Celular"}),(0,r.Y)(b.Ec,{asChild:!0,className:"Control ",children:(0,r.Y)(w.TextField.Root,{placeholder:"Celular",type:"tel"})})]})})]})]})}),(0,r.FD)(w.Tabs.Content,{css:{"&[data-orientation='vertical']":{width:"100%",margin:null}},value:"tab2",children:[(0,r.FD)(w.Card,{css:{align:"center",padding:"36px",width:"50%"},size:"3",children:[(0,r.Y)(b.D0,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"username",children:(0,r.FD)(w.Flex,{direction:"column",children:[(0,r.Y)(b.JU,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Nombre Usuario"}),(0,r.Y)(b.Ec,{asChild:!0,className:"Control ",children:(0,r.Y)(w.TextField.Root,{placeholder:"Username",type:"text"})})]})}),(0,r.Y)(b.D0,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"clave",children:(0,r.FD)(w.Flex,{direction:"column",children:[(0,r.Y)(b.JU,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Contrase\xf1a"}),(0,r.Y)(b.Ec,{asChild:!0,className:"Control ",children:(0,r.Y)(w.TextField.Root,{placeholder:"Password",type:"password"})})]})}),(0,r.Y)(b.D0,{className:"Field ",css:{display:"grid",marginBottom:"10px",width:"100%"},name:"conclave",children:(0,r.FD)(w.Flex,{direction:"column",children:[(0,r.Y)(b.JU,{className:"Label ",css:{fontSize:"15px",fontWeight:"500",lineHeight:"35px"},children:"Confirmacion Contrase\xf1a"}),(0,r.Y)(b.Ec,{asChild:!0,className:"Control ",children:(0,r.Y)(w.TextField.Root,{placeholder:"Confirmar Password",type:"password"})})]})})]}),(0,r.Y)(b.XT,{asChild:!0,className:"Submit ",children:(0,r.Y)(w.Button,{css:{width:"50%",height:"100%",display:"block",padding:"15px",borderRadius:"1em","&:hover":{backgroundColor:"#a6ccb9"}},children:"Enviar"})})]})]})})}let V=(0,d.keyframes)(_());function S(){let[e,i]=(0,o.useContext)(a.EventLoopContext);return(0,r.Y)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: "+(i.length>0?i[i.length-1].message:""),children:(0,r.Y)(H,{})})}function N(){let[e,i]=(0,o.useContext)(a.EventLoopContext),n=(0,o.useRef)(null);l.refs.ref_mi_box_base=n;let t=(0,o.useCallback)((i,n)=>e([(0,l.Event)("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception",{stack:i.stack,component_stack:n.componentStack},{})],[i,n],{}),[e,l.Event]);return(0,r.FD)(c.tH,{fallbackRender:i=>(0,d.jsx)("div",{css:{height:"100%",width:"100%",position:"absolute",display:"flex",alignItems:"center",justifyContent:"center"}},(0,d.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem"}},(0,d.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem",maxWidth:"50ch",border:"1px solid #888888",borderRadius:"0.25rem",padding:"1rem"}},(0,d.jsx)("h2",{css:{fontSize:"1.25rem",fontWeight:"bold"}},(0,d.jsx)(o.Fragment,{},"An error occurred while rendering this page.")),(0,d.jsx)("p",{css:{opacity:"0.75"}},(0,d.jsx)(o.Fragment,{},"This is an error with the application itself.")),(0,d.jsx)("details",{},(0,d.jsx)("summary",{css:{padding:"0.5rem"}},(0,d.jsx)(o.Fragment,{},"Error message")),(0,d.jsx)("div",{css:{width:"100%",maxHeight:"50vh",overflow:"auto",background:"#000",color:"#fff",borderRadius:"0.25rem"}},(0,d.jsx)("div",{css:{padding:"0.5rem",width:"fit-content"}},(0,d.jsx)("pre",{},(0,d.jsx)(o.Fragment,{},i.error.stack)))),(0,d.jsx)("button",{css:{padding:"0.35rem 0.75rem",margin:"0.5rem",background:"#fff",color:"#000",border:"1px solid #000",borderRadius:"0.25rem",fontWeight:"bold"},onClick:function(){for(var n=arguments.length,t=Array(n),r=0;r<n;r++)t[r]=arguments[r];return e([(0,l.Event)("_call_function",{function:()=>navigator.clipboard.writeText(i.error.stack),callback:null},{})],t,{})}},(0,d.jsx)(o.Fragment,{},"Copy")))),(0,d.jsx)("hr",{css:{borderColor:"currentColor",opacity:"0.25"}}),(0,d.jsx)("a",{href:"https://reflex.dev"},(0,d.jsx)("div",{css:{display:"flex",alignItems:"baseline",justifyContent:"center",fontFamily:"monospace","--default-font-family":"monospace",gap:"0.5rem"}},(0,d.jsx)(o.Fragment,{},"Built with "),(0,d.jsx)("svg",{"aria-label":"Reflex",css:{fill:"currentColor"},height:"12",role:"img",width:"56",xmlns:"http://www.w3.org/2000/svg"},(0,d.jsx)("path",{d:"M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z"}),(0,d.jsx)("path",{d:"M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z"}),(0,d.jsx)("path",{d:"M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z"}),(0,d.jsx)("path",{d:"M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z"}),(0,d.jsx)("path",{d:"M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z"}),(0,d.jsx)("path",{d:"M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z"}),(0,d.jsx)("title",{},(0,d.jsx)(o.Fragment,{},"Reflex"))))))),onError:t,children:[(0,r.FD)(o.Fragment,{children:[(0,r.Y)(S,{}),(0,r.Y)(k,{})]}),(0,r.FD)(w.Box,{id:"mi-box-base",ref:n,children:[(0,r.Y)(w.Box,{css:{size:"3",align:"center",padding:"36px"},children:(0,r.FD)(w.Card,{css:{padding:"15px",borderRadius:"8px"},size:"2",children:[(0,r.FD)(w.Flex,{align:"start",className:"rx-Stack",css:{height:"100%",alignItems:"center",width:"100%"},direction:"row",gap:"4",children:[(0,r.Y)(w.Badge,{color:"blue",css:{padding:"0.65rem"},radius:"full",children:(0,r.Y)(m.A,{css:{color:"var(--current-color)"},size:32})}),(0,r.FD)(w.Flex,{align:"start",className:"rx-Stack",css:{height:"100%"},direction:"column",gap:"1",children:[(0,r.Y)(w.Heading,{size:"4",weight:"bold",children:"Registro de Usuarios"}),(0,r.Y)(w.Text,{as:"p",size:"2",children:"Gracias por su Confianza"})]})]}),(0,r.Y)(y,{})]})}),(0,r.Y)(s.cG,{}),(0,r.Y)("footer",{css:{width:"100%",background:"#492D99"},children:(0,r.FD)(w.Flex,{align:"start",className:"rx-Stack",css:{width:"100%"},direction:"column",gap:"5",children:[(0,r.Y)(w.Separator,{size:"4"}),(0,r.FD)(w.Flex,{css:{"@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"column"},"@media screen and (min-width: 48em)":{flexDirection:"row"},width:"100%"},justify:"between",gap:"6",children:[(0,r.FD)(w.Flex,{align:"start",className:"rx-Stack",css:{"@media screen and (min-width: 0)":{alignItems:"center"},"@media screen and (min-width: 30em)":{alignItems:"center"},"@media screen and (min-width: 48em)":{alignItems:"start"}},direction:"column",gap:"4",children:[(0,r.Y)(w.Flex,{align:"start",className:"rx-Stack",css:{alignItems:"center"},direction:"row",gap:"3",children:(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,r.Y)(D(),{href:"/",passHref:!0,children:(0,r.FD)(w.Flex,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,r.Y)("img",{css:{width:"4em",height:"auto",borderRadius:"25%"},src:"/logoCPK.jpg"}),(0,r.Y)(w.Heading,{css:{color:"#1B7348"},size:"7",weight:"bold",children:""})]})})})}),(0,r.Y)(w.Text,{as:"p",css:{whiteSpace:"nowrap",color:"#88D62A"},size:"3",weight:"medium",children:"Otra Forma de Moverse  \xa9 2024 "}),(0,r.Y)(w.Text,{as:"p",css:{whiteSpace:"nowrap",color:"#88D62A"},size:"3",weight:"medium",children:"Email: contacto@cpkm.com.co"}),(0,r.Y)(w.Text,{as:"p",css:{whiteSpace:"nowrap",color:"#88D62A"},size:"3",weight:"medium",children:"Mobil: +57 3152 225226"})]}),(0,r.FD)(w.Flex,{css:{"@media screen and (min-width: 0)":{textAlign:"center"},"@media screen and (min-width: 30em)":{textAlign:"center"},"@media screen and (min-width: 48em)":{textAlign:"start"},flexDirection:"column"},gap:"2",children:[(0,r.Y)(w.Heading,{css:{width:"100%",paddingTop:"0.8em",padding:"0.8em",color:"#88D62A"},children:"PRODUCTOS"}),(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,r.Y)(D(),{href:"/productos",passHref:!0,children:(0,r.Y)(w.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Neum\xe1ticos Reencauchados"})})}),(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,r.Y)(D(),{href:"/productos",passHref:!0,children:(0,r.Y)(w.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Neum\xe1ticos Nuevos"})})})]}),(0,r.FD)(w.Flex,{css:{"@media screen and (min-width: 0)":{textAlign:"center"},"@media screen and (min-width: 30em)":{textAlign:"center"},"@media screen and (min-width: 48em)":{textAlign:"start"},flexDirection:"column"},gap:"2",children:[(0,r.Y)(w.Heading,{css:{width:"100%",paddingTop:"0.8em",padding:"0.8em",color:"#88D62A"},children:"SERVICIOS"}),(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,r.Y)(D(),{href:"/servicios",passHref:!0,children:(0,r.Y)(w.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Leasing de Neum\xe1ticos"})})}),(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,r.Y)(D(),{href:"/servicios",passHref:!0,children:(0,r.Y)(w.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Reembolsos"})})})]})]}),(0,r.Y)(w.Separator,{size:"4"}),(0,r.FD)(w.Flex,{align:"start",className:"rx-Stack",css:{width:"100%"},direction:"row",justify:"between",gap:"3",children:[(0,r.FD)(w.Flex,{align:"center",className:"rx-Stack",css:{width:"100%"},direction:"row",gap:"6",children:[(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,r.Y)(D(),{href:"/#",passHref:!0,children:(0,r.Y)(w.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Privacy Policy"})})}),(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,r.Y)(D(),{href:"/#",passHref:!0,children:(0,r.Y)(w.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Terms of Service"})})}),(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,r.Y)(D(),{href:"/#",passHref:!0,children:(0,r.Y)(w.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Developer: REDx Soluciones"})})})]}),(0,r.FD)(w.Flex,{css:{width:"100%"},justify:"end",gap:"3",children:[(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"},color:"#88D62A"},children:(0,r.Y)(D(),{href:"/#",passHref:!0,children:(0,r.Y)(x.A,{css:{color:"var(--current-color)"}})})}),(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"},color:"#88D62A"},children:(0,r.Y)(D(),{href:"/#",passHref:!0,children:(0,r.Y)(p.A,{css:{color:"var(--current-color)"}})})}),(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"},color:"#88D62A"},children:(0,r.Y)(D(),{href:"/#",passHref:!0,children:(0,r.Y)(g.A,{css:{color:"var(--current-color)"}})})}),(0,r.Y)(w.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"},color:"#88D62A"},children:(0,r.Y)(D(),{href:"/#",passHref:!0,children:(0,r.Y)(f.A,{css:{color:"var(--current-color)"}})})})]})]}),(0,r.Y)(w.Separator,{size:"4"})]})})]}),(0,r.FD)(C(),{children:[(0,r.Y)("title",{children:"CPK Usuarios"}),(0,r.Y)("meta",{content:"favicon.ico",property:"og:image"})]})]})}function z(){return(0,r.FD)(o.Fragment,{children:[(0,r.Y)(s.uV,{}),(0,r.Y)(N,{})]})}},8526:(e,i,n)=>{"use strict";n.d(i,{cG:()=>f,uP:()=>p,uV:()=>m});var t=n(2445),r=n(9188),o=n(6540),s=n(2930),c=n(8779),a=n(4953),l=n.n(a),d=n(6818),h=n(1295);function m(){let{resolvedColorMode:e}=(0,o.useContext)(r.ColorModeContext);return(0,t.FD)("a",{css:{position:"fixed",bottom:"1rem",right:"1rem",display:"flex","flex-direction":"row",gap:"0.375rem","align-items":"center",width:"auto","border-radius":"0.5rem",color:"light"===e?"#E5E7EB":"#27282B",border:"light"===e?"1px solid #27282B":"1px solid #E5E7EB","background-color":"light"===e?"#151618":"#FCFCFD",padding:"0.375rem",transition:"background-color 0.2s ease-in-out","box-shadow":"0 1px 2px 0 rgba(0, 0, 0, 0.05)","z-index":"9998",cursor:"pointer",align:"center",textAlign:"center"},href:"https://reflex.dev",target:"_blank",children:[(0,t.FD)("svg",{css:{fill:"white",viewBox:"0 0 16 16"},height:"16",width:"16",xmlns:"http://www.w3.org/2000/svg",children:[(0,t.Y)("rect",{css:{fill:"#6E56CF"},height:"16",rx:"2",width:"16"}),(0,t.Y)("path",{css:{fill:"white"},d:"M10 9V13H12V9H10Z"}),(0,t.Y)("path",{css:{fill:"white"},d:"M4 3V13H6V9H10V7H6V5H10V7H12V3H4Z"})]}),(0,t.Y)(c.Box,{css:{"@media screen and (min-width: 0)":{display:"none"},"@media screen and (min-width: 30em)":{display:"none"},"@media screen and (min-width: 48em)":{display:"none"},"@media screen and (min-width: 62em)":{display:"block"}},children:(0,t.Y)(c.Text,{as:"p",css:{color:"var(--slate-1)",fontWeight:"600",fontFamily:"'Instrument Sans', sans-serif","--default-font-family":"'Instrument Sans', sans-serif",fontSize:"0.875rem",lineHeight:"1rem",letterSpacing:"-0.00656rem"},children:"Built with Reflex"})})]})}let x=l()(()=>Promise.all([n.e(197),n.e(300)]).then(n.t.bind(n,3300,23)),{loadableGenerated:{webpack:()=>[3300]},ssr:!1});function p(){let e=(0,o.useContext)(r.StateContexts.reflex___state____state__link_bio___components___navbar____moment_state);return(0,t.Y)(x,{format:"YYYY-MM-DD",children:e.date_now})}function g(){let{resolvedColorMode:e}=(0,o.useContext)(r.ColorModeContext);return(0,t.Y)(o.Fragment,{children:(0,s.isTrue)("light"===e)?(0,t.Y)(o.Fragment,{children:(0,t.Y)(d.A,{css:{color:"var(--current-color)"}})}):(0,t.Y)(o.Fragment,{children:(0,t.Y)(h.A,{css:{color:"var(--current-color)"}})})})}function f(){let e=(0,o.useRef)(null);s.refs.ref_mi_color_modelo_btn=e;let{toggleColorMode:i}=(0,o.useContext)(r.ColorModeContext),[n,a]=(0,o.useContext)(r.EventLoopContext),l=(0,o.useCallback)(i,[n,s.Event,i]);return(0,t.Y)(c.IconButton,{css:{padding:"6px",position:"fixed",bottom:"2rem",left:"2rem",background:"transparent",color:"inherit",zIndex:"20","&:hover":{cursor:"pointer"}},id:"mi-color-modelo-btn",onClick:l,ref:e,children:(0,t.Y)(g,{})})}}},e=>{var i=i=>e(e.s=i);e.O(0,[931,562,636,593,792],()=>i(2546)),_N_E=e.O()}]);