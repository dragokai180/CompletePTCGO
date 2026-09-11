from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4c0b9f79-73e1-58a5-b2bc-efb86ffad3a3',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name',
    display_name='Whimsicott',
    searchable_by=['Whimsicott', 'Stage 1', 'Whimsicott'],
    subtypes=['Stage 1'],
    collector_number=56,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name',
    family_id=546,
    abilities=[
        Attack(
            title='Windy Mischief',
            game_text="Move all damage counters from 1 of your Benched Pokémon to your opponent's Active Pokémon.",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rolling Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
