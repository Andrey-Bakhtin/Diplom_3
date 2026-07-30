
HTML5_DRAG_AND_DROP = """
    function createEvent(type) {
        const e = document.createEvent("CustomEvent");
        e.initCustomEvent(type, true, true, null);
        // Эмулируем dataTransfer так, как его ожидает современный фронтенд
        e.dataTransfer = { 
            data: {}, 
            setData: function(k, v) { this.data[k] = v; }, 
            getData: function(k) { return this.data[k]; } 
        };
        return e;
    }

    function dispatch(el, e, dt) {
        if (dt !== undefined) e.dataTransfer = dt;
        el.dispatchEvent ? el.dispatchEvent(e) : el.fireEvent("on" + e.type, e);
    }

    function simulate(src, dst) {
        // 1. Начало перетаскивания
        const start = createEvent("dragstart");
        dispatch(src, start);
        
        // 2. Бросание 
        const drop = createEvent("drop");
        drop.dataTransfer = start.dataTransfer;
        dispatch(dst, drop);
        
        // 3. Конец перетаскивания 
        const end = createEvent("dragend");
        end.dataTransfer = start.dataTransfer;
        dispatch(src, end);
    }
    
    simulate(arguments[0], arguments[1]);
    """
