from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='448fd7f9-e325-5f83-874f-f65b178d962b',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name',
    display_name='Hariyama',
    searchable_by=['Hariyama', 'Stage 1', 'Hariyama'],
    subtypes=['Stage 1'],
    collector_number=68,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name',
    family_id=296,
    abilities=[
        Attack(
            title='Push Out',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Megaton Slap Push',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
