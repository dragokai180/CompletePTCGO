from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.pokemon import TeraRulePassive


async def euclase(ctx):
    """Knock Out 1 of your opponent's Pokémon that has exactly 6 damage
    counters on it."""
    candidates = []
    for pokemon in ctx.opponent_pokemon_in_play():
        counters = max(0, (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10)
        if counters == 6 and not ctx.effects_blocked(pokemon):
            candidates.append(pokemon)
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon with exactly 6 damage counters"
    )
    if target is not None:
        await ctx.knock_out(target)


card = PokemonCardDef(
    guid="975789b6-a60e-5b91-bcb0-292df14ee3df",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceonex.Name",
    display_name="Glaceon ex",
    searchable_by=["Glaceon ex","Stage 1","ex","Tera","Glaceonex"],
    subtypes=["Stage 1","ex","Tera"],
    collector_number=26,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    family_id=133,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Frost Bullet",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=snipe_attack(30, also_base=True),
        ),
        Attack(
            title="Euclase",
            game_text="Knock Out 1 of your opponent's Pokémon that has exactly 6 damage counters on it.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.DARKNESS: 1},
            effect=euclase,
        ),
    ],
)
