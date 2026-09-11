from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='70079681-4130-537b-91ef-f1ace7347bd1',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scovillain.Name',
    display_name='Scovillain',
    searchable_by=['Scovillain', 'Stage 1', 'Scovillain'],
    subtypes=['Stage 1'],
    collector_number=29,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name',
    family_id=951,
    abilities=[
        Attack(
            title='Hot Bite',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Super Spicy Breath',
            game_text='If this Pokémon has any Fire Energy attached, this attack does 90 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
