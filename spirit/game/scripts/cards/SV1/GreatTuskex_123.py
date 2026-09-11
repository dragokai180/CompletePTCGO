from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4c7877a7-6b14-5f80-9034-81a059282214',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GreatTuskex.Name',
    display_name='Great Tusk ex',
    searchable_by=['Great Tusk ex', 'Basic', 'ex', 'GreatTuskex'],
    subtypes=['Basic', 'ex'],
    collector_number=123,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=984,
    abilities=[
        Attack(
            title='Bedrock Breaker',
            game_text='Discard a Stadium in play.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Gigantic Tusks',
            game_text='This Pokémon also does 50 damage to itself.',
            cost={PokemonTypes.FIGHTING: 3},
            damage=250,
            effect=standard_attack,
        ),
    ],
)
