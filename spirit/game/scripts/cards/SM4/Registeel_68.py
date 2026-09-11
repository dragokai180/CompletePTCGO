from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='770305d0-f68a-5b31-b8f8-225758034d84',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name',
    display_name='Registeel',
    searchable_by=['Registeel', 'Basic', 'Registeel'],
    subtypes=['Basic'],
    collector_number=68,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=379,
    abilities=[
        Attack(
            title='Turbo Arm',
            game_text='Attach a basic Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Iron Hand',
            game_text='If Regice is on your Bench, heal 30 damage from this Pokémon.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
