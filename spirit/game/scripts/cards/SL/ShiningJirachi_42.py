from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e4c15e7-296e-5570-a9ae-2dde1126dc1f',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShiningJirachi.Name',
    display_name='Shining Jirachi',
    searchable_by=['Shining Jirachi', 'Basic', 'ShiningJirachi'],
    subtypes=['Basic'],
    collector_number=42,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Shining,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=385,
    abilities=[
        Attack(
            title='Stellar Reign',
            game_text="If your opponent's Active Pokémon is an evolved Pokémon, devolve it by putting all of the Evolution cards on it into your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
