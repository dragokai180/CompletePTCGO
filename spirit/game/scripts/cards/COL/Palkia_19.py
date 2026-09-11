from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9e38f498-9274-542e-af37-c855df853b71',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name',
    display_name='Palkia',
    searchable_by=['Palkia', 'Basic', 'Palkia'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=484,
    abilities=[
        Attack(
            title='Wormhole',
            game_text='Switch Palkia with 1 of your Benched Pokémon. Then, your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.WATER: 4},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
