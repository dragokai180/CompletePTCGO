from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a88a5c75-7517-5fa1-b774-914cfd8fd9e7',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name',
    display_name='Zweilous',
    searchable_by=['Zweilous', 'Stage 1', 'Zweilous'],
    subtypes=['Stage 1'],
    collector_number=139,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name',
    family_id=633,
    abilities=[
        Attack(
            title='Find a Friend',
            game_text='Search your deck for up to 2 Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
