from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='05553ca1-6410-56ae-b1a6-159f87aa4386',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name',
    display_name='Bunnelby',
    searchable_by=['Bunnelby', 'Basic', 'Bunnelby'],
    subtypes=['Basic'],
    collector_number=111,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=659,
    abilities=[
        Attack(
            title='Dig',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
