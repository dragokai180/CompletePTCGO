from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9bf35b01-62a5-54bd-8a0a-4ff5488e2266',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name',
    display_name='Pawmi',
    searchable_by=['Pawmi', 'Basic', 'Pawmi'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=921,
    abilities=[
        Attack(
            title='Jolt',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
    ],
)
