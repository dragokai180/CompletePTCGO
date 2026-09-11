from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9c6bf2d2-980a-548f-9a5c-0e4f567b64cd',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name',
    display_name='Pawmo',
    searchable_by=['Pawmo', 'Stage 1', 'Pawmo'],
    subtypes=['Stage 1'],
    collector_number=75,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name',
    family_id=921,
    abilities=[
        Attack(
            title='Thunder Shock',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Head Bolt',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
