from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="0d35e76a-5129-50f7-9b85-6284dd4a7600",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareonex.Name",
    display_name="Flareon ex",
    searchable_by=["Flareon ex","Stage 1","ex","Tera","Flareonex"],
    subtypes=["Stage 1","ex","Tera"],
    collector_number=14,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    family_id=133,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Burning Charge",
            game_text="Search your deck for up to 2 Basic Energy cards and attach them to 1 of your Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=search_attach_energy(is_basic_energy_card, count=2, distribute=False),
        ),
        Attack(
            title="Carnelian",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=280,
            locks_next_turn=True,
        ),
    ],
)
