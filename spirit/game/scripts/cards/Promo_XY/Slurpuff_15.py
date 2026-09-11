from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a2238cc-42e7-5c7b-bb22-ba1c1c5936bc',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name',
    display_name='Slurpuff',
    searchable_by=['Slurpuff', 'Stage 1', 'Slurpuff'],
    subtypes=['Stage 1'],
    collector_number=15,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name',
    family_id=685,
    abilities=[
        Attack(
            title='Cotton Guard',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Sleepy Ball',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
