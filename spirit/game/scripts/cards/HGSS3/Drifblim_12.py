from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='960b41be-2647-589c-b836-ed20468ac38c',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name',
    display_name='Drifblim',
    searchable_by=['Drifblim', 'Stage 1', 'Drifblim'],
    subtypes=['Stage 1'],
    collector_number=12,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name',
    family_id=425,
    abilities=[
        Attack(
            title='Balloon Tackle',
            game_text='Drifblim does 20 damage to itself.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Take Away',
            game_text='Shuffle Drifblim and all cards attached to it back into your deck. Then, your opponent shuffles the Defending Pokémon and all cards attached to it into his or her deck. (You choose your new Active Pokémon first.)',
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
