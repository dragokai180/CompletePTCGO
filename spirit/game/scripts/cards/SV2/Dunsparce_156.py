from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0d791f3f-8f52-5213-841e-4b60cd5104fb',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name',
    display_name='Dunsparce',
    searchable_by=['Dunsparce', 'Basic', 'Dunsparce'],
    subtypes=['Basic'],
    collector_number=156,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=206,
    abilities=[
        Attack(
            title='Find a Friend',
            game_text='Search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
