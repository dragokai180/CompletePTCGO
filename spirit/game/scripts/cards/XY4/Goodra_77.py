from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f73a0604-adc7-51b1-818f-200e00ed085f',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name',
    display_name='Goodra',
    searchable_by=['Goodra', 'Stage 2', 'Goodra'],
    subtypes=['Stage 2'],
    collector_number=77,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name',
    family_id=704,
    abilities=[
        Ability(
            title='Slip Trip',
            game_text="Each player can't attach any Pokémon Tool cards from his or her hand to any of his or her Pokémon.",
            passive=standard_passive("Each player can't attach any Pokémon Tool cards from his or her hand to any of his or her Pokémon."),
        ),
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top card of your deck.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
