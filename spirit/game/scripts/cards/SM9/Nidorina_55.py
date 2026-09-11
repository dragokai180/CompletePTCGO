from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='28900f36-a579-5dab-aba3-fdcb11e12add',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name',
    display_name='Nidorina',
    searchable_by=['Nidorina', 'Stage 1', 'Nidorina'],
    subtypes=['Stage 1'],
    collector_number=55,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    family_id=29,
    abilities=[
        Attack(
            title='Family Rescue',
            game_text='Shuffle 5 Psychic Pokémon from your discard pile into your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
