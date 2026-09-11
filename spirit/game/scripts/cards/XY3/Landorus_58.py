from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1124aa45-bd86-5ef5-84d9-7f9ada3d3633',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name',
    display_name='Landorus',
    searchable_by=['Landorus', 'Basic', 'Landorus'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=645,
    abilities=[
        Attack(
            title='Shout of Power',
            game_text='Attach a basic Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Sky Lariat',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)
