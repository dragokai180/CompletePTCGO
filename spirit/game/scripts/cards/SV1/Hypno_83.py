from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='16e908c4-5f34-5de2-a775-6caf391c3a2c',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name',
    display_name='Hypno',
    searchable_by=['Hypno', 'Stage 1', 'Hypno'],
    subtypes=['Stage 1'],
    collector_number=83,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name',
    family_id=96,
    abilities=[
        Attack(
            title='Pendulum Influence',
            game_text="Flip a coin. If heads, choose an attack from 1 of your opponent's Pokémon in play and use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psychic Sphere',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
