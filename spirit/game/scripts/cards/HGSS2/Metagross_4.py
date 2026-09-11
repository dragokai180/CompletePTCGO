from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='075abd3a-710f-5873-a42b-cdc8e360510c',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name',
    display_name='Metagross',
    searchable_by=['Metagross', 'Stage 2', 'Metagross'],
    subtypes=['Stage 2'],
    collector_number=4,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name',
    family_id=374,
    abilities=[
        Ability(
            title='Psychic Float',
            game_text='If you have any Psychic Energy attached to your Active Pokémon, the Retreat Cost for that Pokémon is 0.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('If you have any Psychic Energy attached to your Active Pokémon, the Retreat Cost for that Pokémon is 0.'),
        ),
        Attack(
            title='Pulse Blast',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title='Double Leg Hammer',
            game_text="Choose 2 of your opponent's Benched Pokémon. This attack does 40 damage to each of them. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=standard_attack,
        ),
    ],
)
