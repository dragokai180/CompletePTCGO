from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d5bb200-6cb6-5c80-935f-84cf46158433',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name',
    display_name='Gothitelle',
    searchable_by=['Gothitelle', 'Stage 2', 'Gothitelle'],
    subtypes=['Stage 2'],
    collector_number=54,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name',
    family_id=574,
    abilities=[
        Attack(
            title='Tractorbeam',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. This attack does 30 damage to the new Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Link Blast',
            game_text="If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached to them, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
