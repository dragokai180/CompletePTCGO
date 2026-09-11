from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="114c4185-93ac-5ef6-a74a-a2fd09d62091",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistchaex.Name",
    display_name="Sinistcha ex",
    searchable_by=["Sinistcha ex", "Stage 1", "ex", "Sinistchaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=23,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    family_id=1012,
    abilities=[
        Attack(
            title="Re-Brew",
            game_text="Put 2 damage counters on 1 of your opponent's Pokémon for each Basic Grass Energy card in your discard pile. Then, shuffle those Energy cards into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Matcha Splash",
            game_text="Heal 30 damage from each of your Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
