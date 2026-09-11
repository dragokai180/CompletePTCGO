from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ac380742-d1d1-5069-b32d-c4c4b648ec23',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name',
    display_name='Goomy',
    searchable_by=['Goomy', 'Basic', 'Goomy'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=704,
    abilities=[
        Ability(
            title='Water Down',
            game_text='Whenever you attach a Water Energy card from your hand to this Pokémon, you may search your deck for Goomy and put it onto your Bench. Shuffle your deck afterward.',
            passive=standard_passive('Whenever you attach a Water Energy card from your hand to this Pokémon, you may search your deck for Goomy and put it onto your Bench. Shuffle your deck afterward.'),
        ),
        Attack(
            title='Stampede',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
