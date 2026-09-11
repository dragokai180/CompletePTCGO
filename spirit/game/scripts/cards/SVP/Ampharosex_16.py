from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1b32c8fc-a64b-59c1-a6d0-e107f5d09d98',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ampharosex.Name',
    display_name='Ampharos ex',
    searchable_by=['Ampharos ex', 'Stage 2', 'ex', 'Ampharosex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=16,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name',
    family_id=179,
    abilities=[
        Attack(
            title='Electro Ball',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
        ),
        Attack(
            title='Thunderstrike Tail',
            game_text='You may discard 2 Energy from this Pokémon to have this attack do 100 more damage.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
