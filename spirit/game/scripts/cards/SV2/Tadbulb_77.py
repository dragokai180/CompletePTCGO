from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fcb1c92b-e3df-5c73-8de8-5287d97d7c95',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name',
    display_name='Tadbulb',
    searchable_by=['Tadbulb', 'Basic', 'Tadbulb'],
    subtypes=['Basic'],
    collector_number=77,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=938,
    abilities=[
        Attack(
            title='Thunder Wave',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
