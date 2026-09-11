from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bcce2c32-f740-5105-9ccb-d8b51d8b6a56',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswine.Name',
    display_name='Mamoswine',
    searchable_by=['Mamoswine', 'Stage 2', 'Mamoswine'],
    subtypes=['Stage 2'],
    collector_number=5,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name',
    family_id=220,
    abilities=[
        Attack(
            title='Icy Wind',
            game_text='The Defending Pokémon is now Asleep.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Snowstorm',
            game_text="Does 20 damage to each of your opponent's Benched Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
