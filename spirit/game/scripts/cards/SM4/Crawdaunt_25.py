from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fb703b12-db27-587f-b401-3c5515999c62',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name',
    display_name='Crawdaunt',
    searchable_by=['Crawdaunt', 'Stage 1', 'Crawdaunt'],
    subtypes=['Stage 1'],
    collector_number=25,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name',
    family_id=341,
    abilities=[
        Attack(
            title='Double Claws',
            game_text="Discard 2 Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
