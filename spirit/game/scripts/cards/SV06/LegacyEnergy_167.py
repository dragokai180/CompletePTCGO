from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _LegacyEnergyPassive(Passive):
    """If the holder is Knocked Out by an opponent attack, reduce prizes by 1
    once per game."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        # Apply only to knockouts by damage from an attack, and only the
        # defending player's opponent gets the reduced prize count.
        if not ctx.is_attack_effect() or ctx.player_id == pokemon.owning_player_id:
            return count

        # Only when the knocked-out Pokémon is the one carrying Legacy Energy.
        if carrier_pokemon(carrier) is not pokemon:
            return count

        if getattr(ctx.session, "legacy_energy_prize_reduced", False):
            return count

        ctx.session.legacy_energy_prize_reduced = True
        return max(0, count - 1)


card = EnergyCardDef(
    guid="dc8df4f4-7949-4d82-b710-8eeb268d2c37",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.energy.LegacyEnergy.Name",
    display_name="Legacy Energy",
    searchable_by=["Legacy Energy", "Special", "ACE SPEC", "LegacyEnergy"],
    subtypes=["Special", "ACE SPEC"],
    collector_number=167,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Ace,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    passive=_LegacyEnergyPassive(),
)

