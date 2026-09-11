from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import discard_own_energy
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import search_attach_energy

card = PokemonCardDef(
    guid="c539ebaf-8b8b-5ae1-8efb-d74c84575217",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus","Basic","Thundurus"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="BW2",
    rarity=Rarities.RareUltra,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Charge",
            game_text="Search your deck for a Lightning Energy card and attach it to this Pokémon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(predicate=is_lightning_energy, count=1, to_self=True),
        ),
        Attack(
            title="Disaster Volt",
            game_text="Discard an Energy attached to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=discard_own_energy,
        ),
    ],
)
