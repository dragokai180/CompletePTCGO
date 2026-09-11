from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='88969c97-ee9f-5cf6-83ed-6cc59339d1a4',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rabsca.Name',
    display_name='Rabsca',
    searchable_by=['Rabsca', 'Stage 1', 'Rabsca'],
    subtypes=['Stage 1'],
    collector_number=99,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name',
    family_id=953,
    abilities=[
        Attack(
            title='Revival Blessing',
            game_text='Put a Pokémon from your discard pile onto your Bench.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psybeam',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
