from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7de5c0d4-360b-5adb-aa6c-0db54f8ccc6e',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Qwilfish.Name',
    display_name='Qwilfish',
    searchable_by=['Qwilfish', 'Basic', 'Qwilfish'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=211,
    abilities=[
        Attack(
            title='Offensive Needle',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Poisoned. If tails, the Defending Pokémon is now Paralyzed.',
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
