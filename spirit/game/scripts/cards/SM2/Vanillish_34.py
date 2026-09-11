from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2056546d-9964-53c7-bfb3-5a96ebf6a250',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name',
    display_name='Vanillish',
    searchable_by=['Vanillish', 'Stage 1', 'Vanillish'],
    subtypes=['Stage 1'],
    collector_number=34,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name',
    family_id=582,
    abilities=[
        Attack(
            title='Ice Shard',
            game_text="If your opponent's Active Pokémon is a Fighting Pokémon, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
