from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='563f0480-b37d-52d7-9f1e-3628f2bf5dc4',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name',
    display_name='Florges',
    searchable_by=['Florges', 'Stage 2', 'Florges'],
    subtypes=['Stage 2'],
    collector_number=93,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name',
    family_id=669,
    abilities=[
        Ability(
            title='Blooming Garden',
            game_text='Your Pokémon in play have no Weakness.',
            passive=standard_passive('Your Pokémon in play have no Weakness.'),
        ),
        Attack(
            title='Moonblast',
            game_text="During your opponent's next turn, the Defending Pokémon's attacks do 30 less damage\xa0(before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
