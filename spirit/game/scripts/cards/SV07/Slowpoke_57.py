from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.session.effects import is_pokemon_card

card = PokemonCardDef(
    guid="dd83173a-90b3-564a-b64c-0f3fef43db9d",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke","Basic","Slowpoke"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    family_id=79,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Dangle Tail",
            game_text="Put a Pokémon from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(
                is_pokemon_card, count=1, minimum=1, reveal=False, to="hand",
                prompt="Choose a Pokémon from your discard pile.",
            ),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
