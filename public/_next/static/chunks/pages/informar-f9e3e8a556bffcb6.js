(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[769],{242:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/informar",function(){return n(7835)}])},7835:function(e,t,n){"use strict";n.r(t),n.d(t,{Div_64093a13086094dda35345330da0660b:function(){return C},Errorboundary_0720dd25ea3a5c8c81e92724f1badd01:function(){return x},Fragment_ecc7fc8159e7de57fc1e48e5f03b41bb:function(){return b},Toaster_9d6e054b03c6e5d1bea1c0a5576b4e6d:function(){return v},default:function(){return y}});var r=n(2729),o=n(5944),i=n(4511),s=n(7294),c=n(8039),a=n(9654),l=n(2658),u=n(917),d=n(4712),h=n(3954),f=n(1320),p=n(9008),m=n.n(p);function _(){let e=(0,r._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _=function(){return e},e}let g=(0,u.keyframes)(_());function v(){let{resolvedColorMode:e}=(0,s.useContext)(c.ColorModeContext);a.refs.__toast=d.Am;let[t,n]=(0,s.useContext)(c.EventLoopContext),r={description:"Check if server is reachable at "+(0,a.getBackendURL)(h.Ks).href,closeButton:!0,duration:12e4,id:"websocket-error"},[i,l]=(0,s.useState)(!1);return(0,s.useEffect)(()=>{n.length>=2?i||d.Am.error("Cannot connect to server: ".concat(n.length>0?n[n.length-1].message:"","."),{...r,onDismiss:()=>l(!0)}):(d.Am.dismiss("websocket-error"),l(!1))},[n]),(0,o.tZ)(d.x7,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function x(){let[e,t]=(0,s.useContext)(c.EventLoopContext),n=(0,s.useCallback)((t,n)=>e([(0,a.Event)("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception",{stack:t.stack,component_stack:n.componentStack},{})],[t,n],{}),[e,a.Event]);return(0,o.BX)(i.SV,{FallbackComponent:E,onError:n,children:[(0,o.BX)(s.Fragment,{children:[(0,o.tZ)(C,{}),(0,o.tZ)(v,{})]}),(0,o.tZ)(s.Fragment,{children:(0,o.tZ)(f.Flex,{css:{display:"flex",alignItems:"center",justifyContent:"center"},children:(0,o.BX)(f.Flex,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:[(0,o.tZ)(f.Heading,{size:"lg",children:"Informar"}),(0,o.tZ)(f.Text,{as:"p",children:"Mi pagina informar"})]})})}),(0,o.BX)(m(),{children:[(0,o.tZ)("title",{children:"My Beautiful App"}),(0,o.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}function E(e){let{error:t,resetErrorBoundary:n}=e;return(0,o.BX)("div",{children:[(0,o.tZ)("p",{children:"Ooops...Unknown Reflex error has occured:"}),(0,o.tZ)("p",{css:{color:"red"},children:t.message}),(0,o.tZ)("p",{children:"Please contact the support."})]})}function C(){let[e,t]=(0,s.useContext)(c.EventLoopContext);return(0,o.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: "+(t.length>0?t[t.length-1].message:""),children:(0,o.tZ)(b,{})})}function b(){let[e,t]=(0,s.useContext)(c.EventLoopContext);return(0,o.tZ)(s.Fragment,{children:(0,a.isTrue)(t.length>0)?(0,o.tZ)(s.Fragment,{children:(0,o.tZ)(l.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:g+" 1s infinite"},size:32})}):(0,o.tZ)(s.Fragment,{})})}function y(){return(0,o.tZ)(x,{})}},4511:function(e,t,n){"use strict";n.d(t,{SV:function(){return s}});var r=n(7294);let o=(0,r.createContext)(null),i={didCatch:!1,error:null};class s extends r.Component{constructor(e){super(e),this.resetErrorBoundary=this.resetErrorBoundary.bind(this),this.state=i}static getDerivedStateFromError(e){return{didCatch:!0,error:e}}resetErrorBoundary(){let{error:e}=this.state;if(null!==e){for(var t,n,r=arguments.length,o=Array(r),s=0;s<r;s++)o[s]=arguments[s];null===(t=(n=this.props).onReset)||void 0===t||t.call(n,{args:o,reason:"imperative-api"}),this.setState(i)}}componentDidCatch(e,t){var n,r;null===(n=(r=this.props).onError)||void 0===n||n.call(r,e,t)}componentDidUpdate(e,t){let{didCatch:n}=this.state,{resetKeys:r}=this.props;if(n&&null!==t.error&&function(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];return e.length!==t.length||e.some((e,n)=>!Object.is(e,t[n]))}(e.resetKeys,r)){var o,s;null===(o=(s=this.props).onReset)||void 0===o||o.call(s,{next:r,prev:e.resetKeys,reason:"keys"}),this.setState(i)}}render(){let{children:e,fallbackRender:t,FallbackComponent:n,fallback:i}=this.props,{didCatch:s,error:c}=this.state,a=e;if(s){let e={error:c,resetErrorBoundary:this.resetErrorBoundary};if("function"==typeof t)a=t(e);else if(n)a=(0,r.createElement)(n,e);else if(void 0!==i)a=i;else throw c}return(0,r.createElement)(o.Provider,{value:{didCatch:s,error:c,resetErrorBoundary:this.resetErrorBoundary}},a)}}}},function(e){e.O(0,[49,888,774,179],function(){return e(e.s=242)}),_N_E=e.O()}]);