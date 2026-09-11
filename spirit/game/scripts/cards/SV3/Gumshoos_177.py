from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8767f521-0559-5ee8-9f50-89327abe9d3c',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gumshoos.Name',
    display_name='Gumshoos',
    searchable_by=['Gumshoos', 'Stage 1', 'Gumshoos'],
    subtypes=['Stage 1'],
    collector_number=177,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name',
    family_id=734,
    abilities=[
        Attack(
            title='Headbang',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Crunch',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
