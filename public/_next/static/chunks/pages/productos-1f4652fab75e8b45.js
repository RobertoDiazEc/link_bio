(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[883],{7928:(e,r,t)=>{(window.__NEXT_P=window.__NEXT_P||[]).push(["/productos",function(){return t(3031)}])},3031:(e,r,t)=>{"use strict";t.r(r),t.d(r,{Div_0c4c0d922d990c245023c72baae2d5e1:()=>F,Errorboundary_7aeeeecdc02e9570658d83fb812cdb83:()=>A,Fragment_c179379f847dbcf00ba21f73b0ad1b3d:()=>H,Link_5701bcae45c1f5b251901c26892640bc:()=>S,Toaster_6e6ebf8d7ce589d59b7d382fb7576edf:()=>_,default:()=>j});var i=t(4577),n=t(2445),s=t(6540),o=t(8526),c=t(7665),a=t(9188),d=t(2930),l=t(7437),h=t(5107),m=t(5933),p=t(1544),x=t(6491),g=t(3258),u=t(5236),f=t(5304),w=t(4721),Y=t(749),v=t(8779),D=t(1106),k=t.n(D),b=t(3368),C=t.n(b);function y(){let e=(0,i._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return y=function(){return e},e}function F(){let[e,r]=(0,s.useContext)(a.EventLoopContext);return(0,n.Y)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: "+(r.length>0?r[r.length-1].message:""),children:(0,n.Y)(H,{})})}function H(){let[e,r]=(0,s.useContext)(a.EventLoopContext);return(0,n.Y)(s.Fragment,{children:(0,d.isTrue)(r.length>0)?(0,n.Y)(s.Fragment,{children:(0,n.Y)(h.A,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:z+" 1s infinite"},size:32})}):(0,n.Y)(s.Fragment,{})})}function _(){let{resolvedColorMode:e}=(0,s.useContext)(a.ColorModeContext);d.refs.__toast=w.oR;let[r,t]=(0,s.useContext)(a.EventLoopContext),i={description:"Check if server is reachable at "+(0,d.getBackendURL)(Y.ll).href,closeButton:!0,duration:12e4,id:"websocket-error"},[o,c]=(0,s.useState)(!1);return(0,s.useEffect)(()=>{t.length>=2?o||w.oR.error("Cannot connect to server: ".concat(t.length>0?t[t.length-1].message:"","."),{...i,onDismiss:()=>c(!0)}):(w.oR.dismiss("websocket-error"),c(!1))},[t]),(0,n.Y)(w.l$,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function A(){let[e,r]=(0,s.useContext)(a.EventLoopContext),t=(0,s.useRef)(null);d.refs.ref_mi_box_base=t;let i=(0,s.useCallback)((r,t)=>e([(0,d.Event)("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception",{stack:r.stack,component_stack:t.componentStack},{})],[r,t],{}),[e,d.Event]);return(0,n.FD)(c.tH,{fallbackRender:r=>(0,l.jsx)("div",{css:{height:"100%",width:"100%",position:"absolute",display:"flex",alignItems:"center",justifyContent:"center"}},(0,l.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem"}},(0,l.jsx)("div",{css:{display:"flex",flexDirection:"column",gap:"1rem",maxWidth:"50ch",border:"1px solid #888888",borderRadius:"0.25rem",padding:"1rem"}},(0,l.jsx)("h2",{css:{fontSize:"1.25rem",fontWeight:"bold"}},(0,l.jsx)(s.Fragment,{},"An error occurred while rendering this page.")),(0,l.jsx)("p",{css:{opacity:"0.75"}},(0,l.jsx)(s.Fragment,{},"This is an error with the application itself.")),(0,l.jsx)("details",{},(0,l.jsx)("summary",{css:{padding:"0.5rem"}},(0,l.jsx)(s.Fragment,{},"Error message")),(0,l.jsx)("div",{css:{width:"100%",maxHeight:"50vh",overflow:"auto",background:"#000",color:"#fff",borderRadius:"0.25rem"}},(0,l.jsx)("div",{css:{padding:"0.5rem",width:"fit-content"}},(0,l.jsx)("pre",{},(0,l.jsx)(s.Fragment,{},r.error.stack)))),(0,l.jsx)("button",{css:{padding:"0.35rem 0.75rem",margin:"0.5rem",background:"#fff",color:"#000",border:"1px solid #000",borderRadius:"0.25rem",fontWeight:"bold"},onClick:function(){for(var t=arguments.length,i=Array(t),n=0;n<t;n++)i[n]=arguments[n];return e([(0,d.Event)("_call_function",{function:()=>navigator.clipboard.writeText(r.error.stack),callback:null},{})],i,{})}},(0,l.jsx)(s.Fragment,{},"Copy")))),(0,l.jsx)("hr",{css:{borderColor:"currentColor",opacity:"0.25"}}),(0,l.jsx)("a",{href:"https://reflex.dev"},(0,l.jsx)("div",{css:{display:"flex",alignItems:"baseline",justifyContent:"center",fontFamily:"monospace","--default-font-family":"monospace",gap:"0.5rem"}},(0,l.jsx)(s.Fragment,{},"Built with "),(0,l.jsx)("svg",{"aria-label":"Reflex",css:{fill:"currentColor"},height:"12",role:"img",width:"56",xmlns:"http://www.w3.org/2000/svg"},(0,l.jsx)("path",{d:"M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z"}),(0,l.jsx)("path",{d:"M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z"}),(0,l.jsx)("path",{d:"M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z"}),(0,l.jsx)("path",{d:"M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z"}),(0,l.jsx)("path",{d:"M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z"}),(0,l.jsx)("path",{d:"M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z"}),(0,l.jsx)("title",{},(0,l.jsx)(s.Fragment,{},"Reflex"))))))),onError:i,children:[(0,n.FD)(s.Fragment,{children:[(0,n.Y)(F,{}),(0,n.Y)(_,{})]}),(0,n.FD)(v.Box,{id:"mi-box-base",ref:t,children:[(0,n.FD)(v.Box,{css:{background:"#492D99",padding:"1em",position:"fixed",top:"0px",zIndex:"1000",width:"100%",overflow:"auto"},children:[(0,n.Y)(v.Box,{css:{"@media screen and (min-width: 0)":{display:"none"},"@media screen and (min-width: 30em)":{display:"none"},"@media screen and (min-width: 48em)":{display:"none"},"@media screen and (min-width: 62em)":{display:"block"}},children:(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",css:{alignItems:"center"},direction:"row",justify:"between",gap:"3",children:[(0,n.Y)(v.Flex,{align:"start",className:"rx-Stack",css:{alignItems:"center"},direction:"row",gap:"3",children:(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/",passHref:!0,children:(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,n.Y)("img",{css:{width:"4em",height:"auto",borderRadius:"25%"},src:"/logoCPK.jpg"}),(0,n.Y)(v.Heading,{css:{color:"#88D62A"},size:"7",weight:"bold",children:""})]})})})}),(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",direction:"row",justify:"end",gap:"5",children:[(0,n.Y)(v.Badge,{css:{color:"#88D62A"},children:(0,n.Y)(o.uP,{})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/servicios",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{color:"#88D62A"},size:"4",weight:"medium",children:"Servicios"})})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/productos",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{color:"#88D62A"},size:"4",weight:"medium",children:"Productos"})})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/comunidad",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{color:"#88D62A"},size:"4",weight:"medium",children:"Comunidad"})})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/contactos",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{color:"#88D62A"},size:"4",weight:"medium",children:"Contactos"})})})]})]})}),(0,n.Y)(v.Box,{css:{"@media screen and (min-width: 0)":{display:"block"},"@media screen and (min-width: 30em)":{display:"block"},"@media screen and (min-width: 48em)":{display:"block"},"@media screen and (min-width: 62em)":{display:"none"}},children:(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",css:{alignItems:"center"},direction:"row",justify:"between",gap:"3",children:[(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",css:{alignItems:"center"},direction:"row",gap:"3",children:[(0,n.Y)("img",{css:{width:"2em",height:"auto",borderRadius:"25%"},src:"/logoCPK.jpg"}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/",passHref:!0,children:(0,n.Y)(v.Heading,{size:"7",weight:"bold",children:""})})})]}),(0,n.FD)(v.DropdownMenu.Root,{css:{justify:"end"},children:[(0,n.Y)(v.DropdownMenu.Trigger,{children:(0,n.Y)(m.A,{css:{color:"var(--current-color)"},size:30})}),(0,n.FD)(v.DropdownMenu.Content,{children:[(0,n.Y)(v.DropdownMenu.Item,{children:(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/servicios",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{color:"#88D62A"},size:"4",weight:"medium",children:"Servicios"})})})}),(0,n.Y)(v.DropdownMenu.Item,{children:(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/productos",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{color:"#88D62A"},size:"4",weight:"medium",children:"Productos"})})})}),(0,n.Y)(v.DropdownMenu.Item,{children:(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/comunidad",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{color:"#88D62A"},size:"4",weight:"medium",children:"Comunidad"})})})}),(0,n.Y)(v.DropdownMenu.Item,{children:(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/contactos",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{color:"#88D62A"},size:"4",weight:"medium",children:"Contactos"})})})})]})]})]})})]}),(0,n.FD)(v.Box,{children:[(0,n.Y)(v.Container,{css:{padding:"16px"},size:"3",children:(0,n.Y)(v.Card,{css:{width:"100%",top:"25%",left:"50%",transform:"translate(-50%, -50%)",backgroundColor:"rgba(0, 0, 0, 0.5)",padding:"10px",borderRadius:"5px",position:"absolute"},children:(0,n.Y)(v.Box,{css:{position:"relative",width:"100%"},children:(0,n.Y)("img",{css:{width:"100%",height:"50%",auto:"format"},src:"/imagen/servicio4.jpg"})})})}),(0,n.Y)(v.Container,{css:{padding:"16px"},size:"3",children:(0,n.Y)(v.Card,{css:{color:"white",fontSize:"1em",fontWeight:"bold",padding:"10px",borderRadius:"15px",spacing:"2",width:"100%"}})}),(0,n.FD)(v.Container,{css:{padding:"16px"},size:"3",children:[(0,n.Y)(v.Card,{css:{backgroundColor:"#ECF0F1"},children:(0,n.Y)(v.Heading,{align:"center",css:{width:"100%",paddingTop:"0.8em",padding:"0.8em",color:"#88D62A"},children:"PRODUCTOS CPK"})}),(0,n.Y)(v.Card,{css:{width:"5Ovw",padding:"10px 10px",backgroundColor:"#ECF0F1"},children:(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",css:{alignItems:"center"},direction:"row",gap:"3",children:[(0,n.Y)("img",{css:{width:"30%",height:"auto",margin:"10px"},src:"/imagen/servicio2.jpg"}),(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:[(0,n.Y)(v.Heading,{css:{width:"100%",paddingTop:"0.8em",padding:"0.8em",color:"#88D62A"},children:"Neum\xe1ticos Reencauchados"}),(0,n.Y)(v.Text,{as:"p",css:{width:"100%",padding:"1em",color:"#0f3c4c",listStyleType:"disc"},children:"Llantas reencauchadas de calidad con garant\xeda durante su vida \xfatil."})]})]})}),(0,n.Y)(v.Separator,{color:"mint",size:"4"}),(0,n.Y)(v.Card,{css:{width:"5Ovw",padding:"10px 10px",backgroundColor:"#ECF0F1"},children:(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",css:{alignItems:"center"},direction:"row",gap:"3",children:[(0,n.Y)("img",{css:{width:"30%",height:"auto",margin:"10px"},src:"/imagen/servicio2.jpg"}),(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:[(0,n.Y)(v.Heading,{css:{width:"100%",paddingTop:"0.8em",padding:"0.8em",color:"#88D62A"},children:"Neum\xe1ticos Nuevos"}),(0,n.Y)(v.Text,{as:"p",css:{width:"100%",padding:"1em",color:"#0f3c4c",listStyleType:"disc"},children:"Ofrecemos neum\xe1ticos eficientes para diferentes usos debidamente comprobados.\xa0"})]})]})})]}),(0,n.Y)(v.Container,{css:{padding:"16px",width:"25%"},size:"3",children:(0,n.Y)(v.Flex,{align:"start",className:"rx-Stack",css:{position:"fixed",bottom:"20px",right:"20px","z-index":"1000"},direction:"row",gap:"3",children:(0,n.Y)(S,{})})})]}),(0,n.Y)(o.cG,{}),(0,n.Y)("footer",{css:{width:"100%",background:"#492D99"},children:(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",css:{width:"100%"},direction:"column",gap:"5",children:[(0,n.Y)(v.Separator,{size:"4"}),(0,n.FD)(v.Flex,{css:{"@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"column"},"@media screen and (min-width: 48em)":{flexDirection:"row"},width:"100%"},justify:"between",gap:"6",children:[(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",css:{"@media screen and (min-width: 0)":{alignItems:"center"},"@media screen and (min-width: 30em)":{alignItems:"center"},"@media screen and (min-width: 48em)":{alignItems:"start"}},direction:"column",gap:"4",children:[(0,n.Y)(v.Flex,{align:"start",className:"rx-Stack",css:{alignItems:"center"},direction:"row",gap:"3",children:(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/",passHref:!0,children:(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,n.Y)("img",{css:{width:"4em",height:"auto",borderRadius:"25%"},src:"/logoCPK.jpg"}),(0,n.Y)(v.Heading,{css:{color:"#1B7348"},size:"7",weight:"bold",children:""})]})})})}),(0,n.Y)(v.Text,{as:"p",css:{whiteSpace:"nowrap",color:"#88D62A"},size:"3",weight:"medium",children:"Otra Forma de Moverse  \xa9 2024 "}),(0,n.Y)(v.Text,{as:"p",css:{whiteSpace:"nowrap",color:"#88D62A"},size:"3",weight:"medium",children:"Email: contacto@cpkm.com.co"}),(0,n.Y)(v.Text,{as:"p",css:{whiteSpace:"nowrap",color:"#88D62A"},size:"3",weight:"medium",children:"Mobil: +57 3152 225226"})]}),(0,n.FD)(v.Flex,{css:{"@media screen and (min-width: 0)":{textAlign:"center"},"@media screen and (min-width: 30em)":{textAlign:"center"},"@media screen and (min-width: 48em)":{textAlign:"start"},flexDirection:"column"},gap:"2",children:[(0,n.Y)(v.Heading,{css:{width:"100%",paddingTop:"0.8em",padding:"0.8em",color:"#88D62A"},children:"PRODUCTOS"}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/productos",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Neum\xe1ticos Reencauchados"})})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/productos",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Neum\xe1ticos Nuevos"})})})]}),(0,n.FD)(v.Flex,{css:{"@media screen and (min-width: 0)":{textAlign:"center"},"@media screen and (min-width: 30em)":{textAlign:"center"},"@media screen and (min-width: 48em)":{textAlign:"start"},flexDirection:"column"},gap:"2",children:[(0,n.Y)(v.Heading,{css:{width:"100%",paddingTop:"0.8em",padding:"0.8em",color:"#88D62A"},children:"SERVICIOS"}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/servicios",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Leasing de Neum\xe1ticos"})})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/servicios",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Reembolsos"})})})]})]}),(0,n.Y)(v.Separator,{size:"4"}),(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",css:{width:"100%"},direction:"row",justify:"between",gap:"3",children:[(0,n.FD)(v.Flex,{align:"center",className:"rx-Stack",css:{width:"100%"},direction:"row",gap:"6",children:[(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/#",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Privacy Policy"})})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/#",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Terms of Service"})})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(k(),{href:"/#",passHref:!0,children:(0,n.Y)(v.Text,{as:"p",css:{fontSize:"12px",color:"#88D62A"},size:"2",children:"Developer: REDx Soluciones"})})})]}),(0,n.FD)(v.Flex,{css:{width:"100%"},justify:"end",gap:"3",children:[(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"},color:"#88D62A"},children:(0,n.Y)(k(),{href:"/#",passHref:!0,children:(0,n.Y)(p.A,{css:{color:"var(--current-color)"}})})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"},color:"#88D62A"},children:(0,n.Y)(k(),{href:"/#",passHref:!0,children:(0,n.Y)(x.A,{css:{color:"var(--current-color)"}})})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"},color:"#88D62A"},children:(0,n.Y)(k(),{href:"/#",passHref:!0,children:(0,n.Y)(g.A,{css:{color:"var(--current-color)"}})})}),(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"},color:"#88D62A"},children:(0,n.Y)(k(),{href:"/#",passHref:!0,children:(0,n.Y)(u.A,{css:{color:"var(--current-color)"}})})})]})]}),(0,n.Y)(v.Separator,{size:"4"})]})})]}),(0,n.FD)(C(),{children:[(0,n.Y)("title",{children:"CPK | Productos"}),(0,n.Y)("meta",{content:"favicon.ico",property:"og:image"})]})]})}let z=(0,l.keyframes)(y());function S(){return(0,n.Y)(v.Link,{asChild:!0,css:{textDecoration:"none","&:hover":{color:"var(--accent-8)"},width:"100%"},target:"_blank",children:(0,n.Y)(k(),{href:"https://wa.me/+573152225226?text=Hola%20quiero%20informaci\xf3n",passHref:!0,children:(0,n.Y)(v.Button,{color:"green",css:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"1em","&:hover":{backgroundColor:"#a6ccb9"}},children:(0,n.FD)(v.Flex,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,n.Y)(f.A,{css:{color:"var(--current-color)"}}),(0,n.Y)(v.Text,{as:"p",css:{fontSize:"1em",color:"#88D62A"},children:"Escribenos"})]})})})})}function j(){return(0,n.FD)(s.Fragment,{children:[(0,n.Y)(o.uV,{}),(0,n.Y)(A,{})]})}},8526:(e,r,t)=>{"use strict";t.d(r,{cG:()=>u,uP:()=>x,uV:()=>m});var i=t(2445),n=t(9188),s=t(6540),o=t(2930),c=t(8779),a=t(4953),d=t.n(a),l=t(6818),h=t(1295);function m(){let{resolvedColorMode:e}=(0,s.useContext)(n.ColorModeContext);return(0,i.FD)("a",{css:{position:"fixed",bottom:"1rem",right:"1rem",display:"flex","flex-direction":"row",gap:"0.375rem","align-items":"center",width:"auto","border-radius":"0.5rem",color:"light"===e?"#E5E7EB":"#27282B",border:"light"===e?"1px solid #27282B":"1px solid #E5E7EB","background-color":"light"===e?"#151618":"#FCFCFD",padding:"0.375rem",transition:"background-color 0.2s ease-in-out","box-shadow":"0 1px 2px 0 rgba(0, 0, 0, 0.05)","z-index":"9998",cursor:"pointer",align:"center",textAlign:"center"},href:"https://reflex.dev",target:"_blank",children:[(0,i.FD)("svg",{css:{fill:"white",viewBox:"0 0 16 16"},height:"16",width:"16",xmlns:"http://www.w3.org/2000/svg",children:[(0,i.Y)("rect",{css:{fill:"#6E56CF"},height:"16",rx:"2",width:"16"}),(0,i.Y)("path",{css:{fill:"white"},d:"M10 9V13H12V9H10Z"}),(0,i.Y)("path",{css:{fill:"white"},d:"M4 3V13H6V9H10V7H6V5H10V7H12V3H4Z"})]}),(0,i.Y)(c.Box,{css:{"@media screen and (min-width: 0)":{display:"none"},"@media screen and (min-width: 30em)":{display:"none"},"@media screen and (min-width: 48em)":{display:"none"},"@media screen and (min-width: 62em)":{display:"block"}},children:(0,i.Y)(c.Text,{as:"p",css:{color:"var(--slate-1)",fontWeight:"600",fontFamily:"'Instrument Sans', sans-serif","--default-font-family":"'Instrument Sans', sans-serif",fontSize:"0.875rem",lineHeight:"1rem",letterSpacing:"-0.00656rem"},children:"Built with Reflex"})})]})}let p=d()(()=>Promise.all([t.e(197),t.e(300)]).then(t.t.bind(t,3300,23)),{loadableGenerated:{webpack:()=>[3300]},ssr:!1});function x(){let e=(0,s.useContext)(n.StateContexts.reflex___state____state__link_bio___components___navbar____moment_state);return(0,i.Y)(p,{format:"YYYY-MM-DD",children:e.date_now})}function g(){let{resolvedColorMode:e}=(0,s.useContext)(n.ColorModeContext);return(0,i.Y)(s.Fragment,{children:(0,o.isTrue)("light"===e)?(0,i.Y)(s.Fragment,{children:(0,i.Y)(l.A,{css:{color:"var(--current-color)"}})}):(0,i.Y)(s.Fragment,{children:(0,i.Y)(h.A,{css:{color:"var(--current-color)"}})})})}function u(){let e=(0,s.useRef)(null);o.refs.ref_mi_color_modelo_btn=e;let{toggleColorMode:r}=(0,s.useContext)(n.ColorModeContext),[t,a]=(0,s.useContext)(n.EventLoopContext),d=(0,s.useCallback)(r,[t,o.Event,r]);return(0,i.Y)(c.IconButton,{css:{padding:"6px",position:"fixed",bottom:"2rem",left:"2rem",background:"transparent",color:"inherit",zIndex:"20","&:hover":{cursor:"pointer"}},id:"mi-color-modelo-btn",onClick:d,ref:e,children:(0,i.Y)(g,{})})}},7665:(e,r,t)=>{"use strict";t.d(r,{tH:()=>o});var i=t(6540);let n=(0,i.createContext)(null),s={didCatch:!1,error:null};class o extends i.Component{constructor(e){super(e),this.resetErrorBoundary=this.resetErrorBoundary.bind(this),this.state=s}static getDerivedStateFromError(e){return{didCatch:!0,error:e}}resetErrorBoundary(){let{error:e}=this.state;if(null!==e){for(var r,t,i=arguments.length,n=Array(i),o=0;o<i;o++)n[o]=arguments[o];null===(r=(t=this.props).onReset)||void 0===r||r.call(t,{args:n,reason:"imperative-api"}),this.setState(s)}}componentDidCatch(e,r){var t,i;null===(t=(i=this.props).onError)||void 0===t||t.call(i,e,r)}componentDidUpdate(e,r){let{didCatch:t}=this.state,{resetKeys:i}=this.props;if(t&&null!==r.error&&function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],r=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return e.length!==r.length||e.some((e,t)=>!Object.is(e,r[t]))}(e.resetKeys,i)){var n,o;null===(n=(o=this.props).onReset)||void 0===n||n.call(o,{next:i,prev:e.resetKeys,reason:"keys"}),this.setState(s)}}render(){let{children:e,fallbackRender:r,FallbackComponent:t,fallback:s}=this.props,{didCatch:o,error:c}=this.state,a=e;if(o){let e={error:c,resetErrorBoundary:this.resetErrorBoundary};if("function"==typeof r)a=r(e);else if(t)a=(0,i.createElement)(t,e);else if(void 0!==s)a=s;else throw c}return(0,i.createElement)(n.Provider,{value:{didCatch:o,error:c,resetErrorBoundary:this.resetErrorBoundary}},a)}}},3258:(e,r,t)=>{"use strict";t.d(r,{A:()=>i});let i=(0,t(9279).A)("Facebook",[["path",{d:"M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z",key:"1jg4f8"}]])},1544:(e,r,t)=>{"use strict";t.d(r,{A:()=>i});let i=(0,t(9279).A)("Instagram",[["rect",{width:"20",height:"20",x:"2",y:"2",rx:"5",ry:"5",key:"2e1cvw"}],["path",{d:"M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z",key:"9exkf1"}],["line",{x1:"17.5",x2:"17.51",y1:"6.5",y2:"6.5",key:"r4j83e"}]])},5236:(e,r,t)=>{"use strict";t.d(r,{A:()=>i});let i=(0,t(9279).A)("Linkedin",[["path",{d:"M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z",key:"c2jq9f"}],["rect",{width:"4",height:"12",x:"2",y:"9",key:"mk3on5"}],["circle",{cx:"4",cy:"4",r:"2",key:"bt5ra8"}]])},5933:(e,r,t)=>{"use strict";t.d(r,{A:()=>i});let i=(0,t(9279).A)("Menu",[["line",{x1:"4",x2:"20",y1:"12",y2:"12",key:"1e0a9i"}],["line",{x1:"4",x2:"20",y1:"6",y2:"6",key:"1owob3"}],["line",{x1:"4",x2:"20",y1:"18",y2:"18",key:"yk5zj1"}]])},5304:(e,r,t)=>{"use strict";t.d(r,{A:()=>i});let i=(0,t(9279).A)("MessageCircleMore",[["path",{d:"M7.9 20A9 9 0 1 0 4 16.1L2 22Z",key:"vv11sd"}],["path",{d:"M8 12h.01",key:"czm47f"}],["path",{d:"M12 12h.01",key:"1mp3jc"}],["path",{d:"M16 12h.01",key:"1l6xoz"}]])},6491:(e,r,t)=>{"use strict";t.d(r,{A:()=>i});let i=(0,t(9279).A)("Twitter",[["path",{d:"M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z",key:"pff0z6"}]])}},e=>{var r=r=>e(e.s=r);e.O(0,[931,636,593,792],()=>r(7928)),_N_E=e.O()}]);