from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5a234414-64ee-5ecb-b795-65ae40da74c3',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name',
    display_name='Feraligatr',
    searchable_by=['Feraligatr', 'Stage 2', 'Feraligatr'],
    subtypes=['Stage 2'],
    collector_number=20,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name',
    family_id=158,
    abilities=[
        Attack(
            title='Spinning Tail',
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Surf',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
