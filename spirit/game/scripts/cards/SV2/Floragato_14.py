from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c809fa75-e3f8-526a-86f2-17d7153b4956',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name',
    display_name='Floragato',
    searchable_by=['Floragato', 'Stage 1', 'Floragato'],
    subtypes=['Stage 1'],
    collector_number=14,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name',
    family_id=906,
    abilities=[
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title='Magic Whip',
            game_text="Switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
