from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1542957c-1394-5f02-9c94-1bb677278aff',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name',
    display_name='Slowbro',
    searchable_by=['Slowbro', 'Stage 1', 'Slowbro'],
    subtypes=['Stage 1'],
    collector_number=80,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    family_id=79,
    abilities=[
        Attack(
            title='Big Yawn',
            game_text='Both Active Pokémon are now Asleep.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Laid-Back Tackle',
            game_text='If this Pokémon evolved during this turn, this attack does nothing.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
