from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_per,
    count_discard,
    self_energy_discard_attack,
)
from spirit.game.card_effects.pokemon import TeraRulePassive, is_energy_card


card = PokemonCardDef(
    guid="5dcb95c0-7902-53b0-9139-aec71f83908c",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ceruledgeex.Name",
    display_name="Ceruledge ex",
    searchable_by=["Ceruledge ex", "Stage 1", "ex", "Tera", "Ceruledgeex"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=36,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Abyssal Flames",
            game_text=(
                "This attack does 20 more damage for each Energy card "
                "in your discard pile."
            ),
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(
                count_discard("mine", is_energy_card), 20, base=30,
            ),
        ),
        Attack(
            title="Raging Amethyst",
            game_text="Discard all Energy from this Pokémon.",
            cost={
                PokemonTypes.FIRE: 1,
                PokemonTypes.PSYCHIC: 1,
                PokemonTypes.METAL: 1,
            },
            damage=280,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)
