from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aacbf7a7-9ef4-521f-bfb0-55604c150ddb',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name',
    display_name='Meowstic',
    searchable_by=['Meowstic', 'Stage 1', 'Meowstic'],
    subtypes=['Stage 1'],
    collector_number=59,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name',
    family_id=677,
    abilities=[
        Attack(
            title='Energy Present',
            game_text='Attach up to 2 Energy cards from your hand to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psyshot',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
