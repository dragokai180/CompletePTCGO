from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='178b9fbe-e3b1-5859-9c23-70a703d934bc',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name',
    display_name='Gothorita',
    searchable_by=['Gothorita', 'Stage 1', 'Gothorita'],
    subtypes=['Stage 1'],
    collector_number=53,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name',
    family_id=574,
    abilities=[
        Attack(
            title='Slap',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title='Psybeam',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
