from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="8b5e96b2-2bf5-57f0-8ae0-c3eb433d1257",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiriex.Name",
    display_name="Tatsugiri ex",
    searchable_by=["Tatsugiri ex", "Basic", "Tera", "ex", "Tatsugiriex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=142,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=978,
    abilities=[
        Attack(
            title="Surprise Pump",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=100,
            effect=standard_attack,
        ),
        Attack(
            title="Cinnabar Lure",
            game_text="Look at the top 10 cards of your deck. You may put any number of Pokémon you find there onto your Bench. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
