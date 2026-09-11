from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d6e02f8c-1d0d-5677-8dd5-abc025ebceeb',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name',
    display_name='Donphan',
    searchable_by=['Donphan', 'Stage 1', 'Prime', 'Donphan'],
    subtypes=['Stage 1', 'Prime'],
    collector_number=107,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name',
    family_id=231,
    abilities=[
        Ability(
            title='Exoskeleton',
            game_text='Any damage done to Donphan by attacks is reduced by 20 (after applying Weakness and Resistance).',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('Any damage done to Donphan by attacks is reduced by 20 (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Earthquake',
            game_text="Does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Impact',
            cost={PokemonTypes.FIGHTING: 3},
            damage=90,
        ),
    ],
)
