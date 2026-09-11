from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7632d1f2-673f-5cd5-a335-c97d46585eca',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name',
    display_name='Metang',
    searchable_by=['Metang', 'Stage 1', 'Metang'],
    subtypes=['Stage 1'],
    collector_number=33,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name',
    family_id=374,
    abilities=[
        Attack(
            title='Energy Crane',
            game_text='Search your discard pile for up to 2 Psychic Energy cards and attach them to your Pokémon in any way you like.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psypunch',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
