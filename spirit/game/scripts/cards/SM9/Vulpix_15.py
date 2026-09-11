from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2b1a9911-fbf9-5932-88fb-1fc1a13c750d',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name',
    display_name='Vulpix',
    searchable_by=['Vulpix', 'Basic', 'Vulpix'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=37,
    abilities=[
        Attack(
            title='Tail Whip',
            game_text="Flip a coin. If heads, the Defending Pokémon can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
