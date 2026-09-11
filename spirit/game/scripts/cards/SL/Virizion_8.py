from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b5f4b412-e929-5dbd-b3d7-0a85c7889d9b',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name',
    display_name='Virizion',
    searchable_by=['Virizion', 'Basic', 'Virizion'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=640,
    abilities=[
        Attack(
            title='Wrapped in Wind',
            game_text='You may attach a basic Energy card from your hand to this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Pike',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
